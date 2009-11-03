# $Id$
# Authority: dries
# Upstream: Antonio Diaz Diaz <ant_diaz$teleline,es>

Summary: GNU OCR (Optical Character Recognition) program
Name: ocrad
Version: 0.17
Release: 1%{?dist}
License: GPLv3
Group: Applications/Publishing
URL: http://www.gnu.org/software/ocrad/ocrad.html

Source: http://ftp.gnu.org/gnu/ocrad/ocrad-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Ocrad is the GNU OCR (Optical Character Recognition) program, implemented as 
a filter and based on a feature extraction method. It reads images in pbm 
(bitmap), pgm (greyscale), or ppm (color) formats and produces text in byte 
(8-bit) or UTF-8 formats. It also includes a layout analyzer that is able to 
separate the columns or blocks of text normally found on printed pages. Ocrad 
can be used as a stand-alone console application, or as a backend to other 
programs.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/ocrad
%{_infodir}/ocrad.info.*

%changelog
* Mon Aug 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
