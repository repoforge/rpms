# $Id$
# Authority: matthias

Summary: Client library for TiVo vserver stream support
Name: vstream-client
Version: 1.2
Release: 2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://armory.nicewarrior.org/projects/vstream-client/
Source: http://mirror-unt.nicewarrior.org/vstream-client/vstream-client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a fork off of the vstream library from the tivo-mplayer project. It
has been stripped down to just the client code. If you have vserver installed
on your Tivo (which most tivo hackers do), then you can use this simple
client to stream .ty files from it.


%package devel
Summary: Development files for the vstream-client library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This is a fork off of the vstream library from the tivo-mplayer project. It
has been stripped down to just the client code. If you have vserver installed
on your Tivo (which most tivo hackers do), then you can use this simple
client to stream .ty files from it.

This package contains the required files to develop programs that will use the
vstream-client library.


%prep
%setup


%build
export CFLAGS="%{optflags}"
./configure \
    --bindir=%{_bindir} \
    --incdir=%{_includedir} \
    --libdir=%{_libdir}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs/
%{__mkdir_p} \
    %{buildroot}%{_bindir} \
    %{buildroot}%{_includedir} \
    %{buildroot}%{_libdir}
%{__make} install \
    BINDIR=%{buildroot}%{_bindir} \
    INCDIR=%{buildroot}%{_includedir} \
    LIBDIR=%{buildroot}%{_libdir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_bindir}/vstream-client

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/vstream-client.h
%{_libdir}/libvstream-client.a


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.2-2
- Release bump to drop the disttag number in FC5 build.

* Mon Dec 19 2005 Matthias Saou <http://freshrpms.net/> 1.2-1
- Initial RPM release.

