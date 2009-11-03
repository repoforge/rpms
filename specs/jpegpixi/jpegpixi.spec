# $Id$
# Authority: bert
# Upstream: Martin Dickopp <martin-jpegpixi$zero-based,org>

Summary: JPEG pixel interpolator
Name: jpegpixi
Version: 1.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.zero-based.org/software/jpegpixi/

Source: http://www.zero-based.org/software/jpegpixi/jpegpixi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libjpeg-devel

%description
Jpegpixi interpolates pixels in JPEG images (single pixels, dots,
stripes). This is useful to correct images from a digital camera with
CCD defects. For example, if one pixel is always bright green, this
pixel can be interpolated with jpegpixi.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%doc %{_mandir}/man1/jpeg*.1*
%{_bindir}/jpeg*

%changelog
* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Sat Oct 09 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Oct 05 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Oct 03 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Fri May 07 2004 Dag Wieers <dag@wieers.com> - 0.15.1-1
- Updated to release 0.15.1.

* Mon Apr 19 2004 Bert de Bruijn <bert@debruijn.be> - 0.15.0-1
- Updated to release 0.15.0.

* Sat Mar 06 2004 Bert de Bruijn <bert@debruijn.be> - 0.14.2-1
- Updated to release 0.14.2.

* Thu Apr 24 2003 Bert de Bruijn <bert@debruijn.be> - 0.14-0
- Initial package. (submitted to DAR)
