# $Id$
# Authority: dag

Summary: SIFT Feature Detection implementation
Name: autopano-sift
Version: 2.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://user.cs.tu-berlin.de/~nowozin/autopano-sift/

Source: http://user.cs.tu-berlin.de/~nowozin/autopano-sift/autopano-sift-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-core >= 1.0.2, gtk-sharp >= 1.0.2, mono-winforms >= 1.0.2, monodevelop >= 0.5.1
Requires: mono-core >= 1.0.2, gtk-sharp >= 1.0.2, mono-winforms >= 1.0.2

%description
The SIFT algorithm provides the capability to identify key feature
points within arbitrary images. It further extracts highly distinct
information for each such point and allows to characterize the point
invariant to a number of modifications to the image. It is invariant
to contrast/brightness changes, to rotation, scaling and partially
invariant to other kinds of transformations.  The algorithm can be
flexibly used to create input data for image matching, object
identification and other computer vision related algorithms.

This package provides an implementation of the SIFT algorithm and a
set of utilities to utilize the algorithm to match two or more images.
As output, a number of control points are created, which specify one
and the same image location in two images. The output is created as
project file for the hugin panorama stitching software, which is
available at http://hugin.sf.net/

%prep
%setup

%build
%{__make} -C src

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/libsift.dll %{buildroot}%{_libdir}/libsift.dll
%{__install} -Dp -m0755 src/util/autopanog/autopanog.exe %{buildroot}%{_bindir}/autopanog.exe
%{__install} -Dp -m0755 src/util/autopano.exe %{buildroot}%{_bindir}/autopano.exe
%{__install} -Dp -m0755 src/util/showone.exe %{buildroot}%{_bindir}/showone.exe
%{__install} -Dp -m0755 src/util/showtwo.exe %{buildroot}%{_bindir}/showtwo.exe
%{__install} -Dp -m0755 src/util/generatekeys.exe %{buildroot}%{_bindir}/generatekeys.exe
%{__install} -Dp -m0755 src/util/generatekeys-sd.exe %{buildroot}%{_bindir}/generatekeys-sd.exe
%{__install} -Dp -m0755 src/bin/autopano-complete.sh %{buildroot}%{_bindir}/autopano-complete.sh
%{__install} -Dp -m0755 src/util/monoopt.sh %{buildroot}%{_bindir}/monoopt.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES doc/* src/doc/* src/TODO
%{_bindir}/autopanog.exe
%{_bindir}/autopano.exe
%{_bindir}/showone.exe
%{_bindir}/showtwo.exe
%{_bindir}/generatekeys.exe
%{_bindir}/generatekeys-sd.exe
%{_bindir}/autopano-complete.sh
%{_bindir}/monoopt.sh
%{_libdir}/libsift.dll

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 16 2005 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 2.1-1
- Initial package. (using DAR)
