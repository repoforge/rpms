# $Id$
# Authority: dag

Summary: Portable archiver
Name: peazip
Version: 1.11
Release: 1%{?dist}
License: LGPL
Group: Applications/File
URL: http://peazip.sourceforge.net/

Source: http://dl.sf.net/peazip/peazip-1.11.src.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PeaZip is a cross-platform portable file archiver, released under LGPL.

    Create: 7z, 7z-sfx, ARC/WRC, BZ2, GZ, LPAQ, PAQ, PEA, QUAD, split, TAR,
            UPX, ZIP;
    Read: 7Z, ARC/WRC, ACE, ARJ, BZ2/TBZ2, CAB, CHM, CPIO, DEB, GZ/TGZ, ISO,
            JAR/EAR/WAR, LZH, NSIS, OOo, PAK/PK3/PK4, PAQ, PEA, PET/PUP,
            QUAD, RAR, RPM, SLP, split, TAR, WIM, XPI, Z/TZ, ZIP;

PeaZip allows to browse archives in navigational or flat mode, to apply
multiple inclusion and exclusion filters to archives, to extract multiple
archives at once.

PeaZip can save, restore, merge and edit archives layout; favourite archive
formats can be saved into a quick access popup menu; format options
(compression, encryption etc) can be finely tuned. The program also allows
to save job definition as command line and to have a detailed job log after
each operation.

PeaZip can be used also to split/merge files in multiple volumes, compress
executables with split/UPX, generate random passwords and keyfiles, benchmark
system (MIPS and Core 2 Duo equivalent MHz rating), compare, checksum/hash
and wipe files.

%prep
%setup -n %{name}-%{version}.src

%build

%install
%{__rm} -rf %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
