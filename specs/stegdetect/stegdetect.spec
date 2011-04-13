# $Id$
# Authority: dag

%{?el6:%define _without_gtk 1}
%{?el5:%define _without_gtk 1}

Summary: Detect and extract steganography messages inside JPEG
Name: stegdetect
Version: 0.6
Release: 1%{?dist}
License: BSD
Group: Applications/File
URL: http://www.outguess.org/detection.php

Source0: http://www.outguess.org/stegdetect-%{version}.tar.gz
Patch0: stegdetect-0.6-configure.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{!?_without_gtk:BuildRequires: gtk+-devel}

%description
Stegdetect is an automated tool for detecting steganographic content in
images. It is capable of detecting several different steganographic
methods to embed hidden information in JPEG images. Currently, the
detectable schemes are jsteg, jphide, invisible secrets, outguess 01.3b,
F5, appendX, and camouflage. Using linear discriminant analysis, it also
supports detection of new stego systems. Stegbreak is used to launch
dictionary attacks against JSteg-Shell, JPHide, and OutGuess 0.13b.

%prep
%setup
%patch0 -p1

%{__perl} -pi -e 's|debug|stegdebug|g' stegdetect.c

%build
%configure --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" SUBDIRS=""

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/stegbreak.1*
%doc %{_mandir}/man1/stegdetect.1*
%{_bindir}/stegbreak
%{_bindir}/stegcompare
%{_bindir}/stegdeimage
%{_bindir}/stegdetect
%{!?_without_gtk:%{_bindir}/xsteg}

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.6-1
- Initial package. (using DAR)
