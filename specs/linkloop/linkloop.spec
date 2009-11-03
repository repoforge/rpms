# $Id$
# Authority: dag
# Upstream: 

Summary: Tool to test connectivity at the link layer (layer 2)
Name: linkloop
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sourceforge.net/projects/linkloop/

Source: http://dl.sf.net/linkloop/linkloop-%{version}-hp.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
linkloop is a similar tool to ping, but tests connectivity at the link layer
(layer 2) instead of the network layer (layer 3). It works like the HP-UX
linkloop utility.

%prep
%setup -n %{name}-%{version}-hp

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" linkloop_replydir="%{_initrddir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/linkloop.1*
%config %{_initrddir}/linkloopd
%{_bindir}/lanscan
%{_bindir}/linkloop_reply
%{_bindir}/linkloop

%changelog
* Fri Apr 27 2007 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
