# $Id$
# Authority: dag
# Upstream: Andrew Mihal <mihal$eecs,berkeley,edu>

Summary: Image Blending with Multiresolution Splines
Name: enblend
Version: 1.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www-cad.eecs.berkeley.edu/~mihal/enblend/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www-cad.eecs.berkeley.edu/~mihal/enblend/enblend-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtiff-devel

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
%doc %{_mandir}/man?/*
%{_bindir}

%changelog
* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
