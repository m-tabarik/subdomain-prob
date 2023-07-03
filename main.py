import subprocess

input_file = 'urls.txt'  # Path to the input file containing URLs
output_file = 'responsive_urls.txt'  # Path to the output file for  responsive URLs

with open(input_file, 'r') as file :
    urls = file.read().splitlines()

responsive_urls = []

for url in urls:
    try:
        subprocess.check_output(['ping', '-c', '1', url])  # Ping the URL
        responsive_urls.append(url)
    except subprocess.CalledProcessError:
        pass  # Ignore if the URL is unresponsive

with open(output_file, 'w') as file:
    file.write('\n'.join(responsive_urls))



print(f"Responsive URLs written to {output_file}")

