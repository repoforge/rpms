# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Shawn Grimes <shawn@aimsniff.com>
# Upstream: <aimsniff-devel@lists.sf.net>

%define real_version 0.9d

Summary: Monitor and archive AOL Instant Messenger messages
Name: aimsniff
Version: 0.9
Release: 0.d
License: GPL
Group: Applications/Internet
URL: http://www.aimsniff.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.aimsniff.com/releases/aimsniff-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
AIM Sniff is a utility for monitoring and archiving AOL Instant Messenger 
messages across a network. Aim Sniff can either do a live dump (actively
sniff the network) or read a PCAP file and parse the file for IM messages.
Aim Sniff also has the option of dumping the information to a MySQL
database or STDOUT. 

%prep
%setup -n %{name}-%{real_version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.9-0.d
- Initial package. (using DAR)
