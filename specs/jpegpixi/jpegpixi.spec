# $Id$

# Authority: dag
# Upstream: Martin Dickopp <martin-jpegpixi@zero-based.org>

Summary: JPEG pixel interpolator.
Name: jpegpixi
Version: 0.14.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.zero-based.org/software/jpegpixi/

Packager: Bert de Bruijn <bert@debruijn.be>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.zero-based.org/software/jpegpixi/jpegpixi-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Jpegpixi interpolates pixels in JPEG images (single pixels, dots, 
stripes). This is useful to correct images from a digital camera with 
CCD defects. For example, if one pixel is always bright green, this 
pixel can be interpolated with jpegpixi.

%prep
%setup

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 jpegpixi jpeghotp %{buildroot}%{_bindir}
%{__install} -m0644 jpegpixi.1 jpeghotp.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Mar 06 2004 Bert de Bruijn <bert@debruijn.be> - 0.14.2-1
- Updated to release 0.14.2.

* Thu Apr 24 2003 Bert de Bruijn <bert@debruijn.be> - 0.14-0
- Initial package. (submitted to DAR)
