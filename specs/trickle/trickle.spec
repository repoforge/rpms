# Authority: dag

# Upstream: marius aamodt eriksen <marius@monkey.org>

### FIXME: Makefiles don't allow -jX (parallel compilation) with -j5
# Distcc: 0

### FIXME: Create a proper sysv script for trickled based on the template.

Summary: A portable lightweight userspace bandwidth shaper.
Name: trickle
Version: 1.06
Release: 0
License: BSD
Group: Applications/Internet
URL: http://www.monkey.org/~marius/trickle/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.monkey.org/~marius/trickle/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libevent-devel

%description
trickle is a portable lightweight userspace bandwidth shaper. It can run
in collaborative mode (together with trickled) or in stand alone mode.

trickle works by taking advantage of the unix loader preloading.
Essentially it provides, to the application, a new version of the
functionality that is required to send and receive data through sockets.
It then limits traffic based on delaying the sending and receiving of
data over a socket. trickle runs entirely in userspace and does not
require root privileges.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/trickle/

%changelog
* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 1.06
- Initial package. (using DAR)
