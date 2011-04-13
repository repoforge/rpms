# $Id$
# Authority: dag

Summary: Crypto Tunnel for Proxying and Forwarding TCP Connections
Name: ctunnel
Version: 0.6
Release: 1%{?dist}
License: GPLv2
Group: Aapplications/Internet
URL: http://nardcore.org/ctunnel/

Source: http://www.nardcore.org/ctunnel/ctunnel-%{version}.tar.gz
Patch0: ctunnel-0.6-makefile.patch
BuildRoot: %{_tmppath}/build-%{name}-%{version}

BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: libgcrypt-devel
BuildRequires: zlib-devel

%description
ctunnel is a software for proxying and forwarding TCP connections via a
cryptographic tunnel.

ctunnel can be used to secure any existing TCP based protocol, such as HTTP,
VNC, Telnet, FTP, RSH, MySQL, etc, as well as UDP.
You can even tunnel SSH! (if you are really paranoid!).

You can also chain/bounce connections to any number of intermediary hosts.

%prep
%setup
%patch0

%build
%{__make} %{?_smp_mflags} \
   PREFIX="%{_prefix}" \
   MANDIR="%{_mandir}" \
   CC="%{__cc}" \
   CRYPTO_TYPE="GCRYPT" \
   OPTFLAGS="%{optflags} -Wall"

%install
%{__make} install DESTDIR="%{buildroot}" \
   PREFIX="%{_prefix}" \
   MANDIR="%{_mandir}" \
   CRYPTO_TYPE="GCRYPT"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%doc %{_mandir}/man1/ctunnel.1*
%{_bindir}/ctunnel

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.6-1
- Initial package. (using DAR)
