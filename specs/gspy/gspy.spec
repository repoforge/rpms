# $Id$
# Authority: dag

Summary: GNOME security camera
Name: gspy
Version: 0.1.7
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://gspy.sourceforge.net/

Source: http://gspy.sf.net/gspy-%{version}-src.tar.gz
Patch0: gspy-configure.patch
Patch1: gspy-autogen.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, autoconf, automake, gtk+-devel
BuildRequires: gnome-libs-devel, intltool, gettext
%{?fc4:BuildRequires: gettext-devel}

%description
Gspy retrieves images from a video4linux device and processes these
into a daily mpeg movie on the disk drive. Each image is recorded
with a time stamp to insure accurate real world correlation. Special
motion detection algorithms are used to reduce the size of the daily
movies by eliminating pictures with similar content as well as the
normal compression obtained via the mpeg process.

%prep
%setup -n %{name}
%patch0
%patch1
%{__perl} -pi -e 's|intl/Makefile||g;' configure.in

%build
#configure
./autogen.sh
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0744)
%{_bindir}/*
%{_datadir}/pixmaps/gv4l/gv4l.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.7-0.2
- Rebuild for Fedora Core 5.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 1.91
- Initial package. (using DAR)
