# $Id$

# Authority: dag
# Upstream: Stef Van Dessel <stef@iguana.be>

%define rversion 20020930

Summary: Download, upload, decode and/or encode "Bommanews"-encoded files.
Name: bnews-utils
Version: 0.0.%{rversion}
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.iguana.be/~stef/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.iguana.be/~stef/bnews-utils-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: perl
Requires: perl

%description
bnews-utils is a series of programs that allow you to download, upload,
decode and/or encode "Bommanews"-encoded files on an NNTP-like network.

For more technical information about this encoding, visit the bnews site.
(http://b-news.sf.net/)

%prep
%setup -n %{name}-%{rversion}

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
%doc AUTHORS ChangeLog COPYING INSTALL LICENSE* NEWS README THANKS TODO
%{_bindir}/*

%changelog
* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.0.20020930-1
- Initial package. (using DAR)
