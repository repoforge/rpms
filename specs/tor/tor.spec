# $Id$
# Authority: dries
# Upstream: EFF

Summary: Send network traffic through virtual tunnels to improve your privacy
Name: tor
Version: 0.1.0.13
Release: 1
License: BSD
Group: Applications/Networking
URL: http://tor.eff.org/

Source: http://tor.eff.org/dist/tor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel, zlib-devel, automake, autoconf, openssl-devel

%description
Tor is a network of virtual tunnels that allows people and groups to improve
their privacy and security on the Internet. It also enables software
developers to create new communication tools with built-in privacy features.
It provides the foundation for a range of applications that allow
organizations and individuals to share information over public networks
without compromising their privacy. Individuals can use it to keep remote
Websites from tracking them and their family members. They can also use it
to connect to resources such as news sites or instant messaging services
that are blocked by their local Internet service providers (ISPs).

%prep
%setup

%build
export CPPFLAGS=-I/usr/include/kerberos
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL LICENSE README
%doc %{_mandir}/man1/tor*
%config(noreplace) %{_sysconfdir}/tor/tor-tsocks.conf
%config(noreplace) %{_sysconfdir}/tor/torrc.sample
%{_bindir}/tor-resolve
%{_bindir}/tor
%{_bindir}/torify

%changelog
* Sat Aug 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.0.13-1
- Update to release 0.1.0.13.

* Sat Jul 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.0.12-1
- Initial package.
