# $Id$
# Authority: dag
# Upstream: Andrew Mihal <mihal$eecs,berkeley,edu>

Summary: Image Blending with Multiresolution Splines
Name: enblend
Version: 3.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://enblend.sourceforge.net/

Source: http://dl.sf.net/enblend/enblend-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtiff-devel, gcc-c++, boost-devel, glew-devel

%description
Enblend is a tool for compositing images. Given a set of images that overlap
in some irregular way, Enblend overlays them in such a way that the seam
between the images is invisible, or at least very difficult to see. Enblend
does not line up the images for you. Use a tool like Hugin to do that.

%prep
%setup

### FIXME: Make configure test use -lm (Please fix upstream)
%{__perl} -pi.orig -e 's|^(  \(eval \$ac_link)(\) 2>&5)$|$1 -lm$2|' configure

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/enblend.1*
%{_bindir}/enblend

%changelog
* Tue Sep  9 2008 Dries Verachtert <dries@ulyssis.org> - 3.2-1
- Updated to release 3.2.

* Sun Jan 28 2007 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Updated to release 3.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.5-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.

* Sat Sep 04 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Updatd to release 1.3.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
