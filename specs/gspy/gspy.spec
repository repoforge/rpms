# $Id$

# Authority: dag

Summary: GNOME security camera.
Name: gspy
Version: 0.1.7
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://gspy.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gspy.sf.net/gspy-%{version}-src.tar.gz
Patch0: gspy-configure.patch
Patch1: gspy-autogen.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gettext

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
%{_bindir}/*
%{_datadir}/pixmaps/gv4l/gv4l.png

%changelog
* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 1.91
- Initial package. (using DAR)
