# Authority: dag
# Upstream: <tcpick-project@lists.sourceforge.net>

Summary: TCP stream sniffer and connection tracker
Name: tcpick
Version: 0.1.21
Release: 1
License: GPL
Group: Applications/Internet
URL: http://tcpick.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/tcpick/tcpick-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


#BuildRequires: 

%description
tcpick is a textmode sniffer that can track tcp streams and saves the data
captured in files or displays them in the terminal. Useful for picking
files in a passive way.

It can store all connections in different files, or it can display all the
stream on the terminal. It is useful to keep track of what users of a network
are doing, and is usable with textmode tools like grep, sed, awk.

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
%doc AUTHORS ChangeLog COPYING INSTALL INTERNALS KNOWN-BUGS NEWS OPTIONS PLATFORMS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.1.21-1
- Initial package. (using DAR)
