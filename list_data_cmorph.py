import calendar
from datetime import datetime
import math

def generate_cmorph_links(start_year=1995, end_year=2024):
    """
    Generate links for CMORPH precipitation data from start_year to end_year
    Format: https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/30min/8km/{year}/{month}/{day}/CMORPH_V1.0_ADJ_8km-30min_{year:04d}{month:02d}{day:02d}{hour:02d}nc
    """
    links = []
    
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Get number of days in the month
            days_in_month = calendar.monthrange(year, month)[1]
            
            for day in range(1, days_in_month + 1):
                for hour in range(0, 24):
                    link = (
                        f"https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/30min/8km/"
                        f"{year}/{month:02d}/{day:02d}/CMORPH_V1.0_ADJ_8km-30min_{year:04d}{month:02d}{day:02d}{hour:02d}.nc"
                    )
                    links.append(link)
    
    return links

def save_links_to_files(links, base_filename="filelist_data", num_files=4):
    """Save the generated links to multiple text files"""
    total_links = len(links)
    links_per_file = math.ceil(total_links / num_files)
    
    for i in range(num_files):
        start_idx = i * links_per_file
        end_idx = min((i + 1) * links_per_file, total_links)
        
        # Skip if no more links to process
        if start_idx >= total_links:
            break
            
        filename = f"{base_filename}{i+1}.txt"
        
        with open(filename, 'w') as f:
            for link in links[start_idx:end_idx]:
                f.write(f"{link}\n")
        
        print(f"File {filename}: {end_idx - start_idx} links (lines {start_idx+1} to {end_idx})")
    
    print(f"\nTotal: {total_links} links split into {num_files} files")

def save_links_to_file(links, filename="filelist_data.txt"):
    """Save the generated links to a single text file (original function)"""
    with open(filename, 'w') as f:
        for link in links:
            f.write(f"{link}\n")
    
    print(f"Generated {len(links)} links and saved to {filename}")

if __name__ == "__main__":
    print("Generating CMORPH data links from 1998 to 2023...")
    links = generate_cmorph_links(1998, 2023)
    
    # Pilihan 1: Simpan ke 4 file terpisah
    print("\nSplitting into 4 files:")
    save_links_to_files(links, "filelist_data", 4)
    
    # Pilihan 2: Simpan ke 1 file (fungsasli)
    # save_links_to_file(links)
    
    print("Done!")