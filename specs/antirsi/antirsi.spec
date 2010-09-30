# $Id$
# Authority: shuff
# Upstream: Onne Gorter <o.gorter$gmail,com>

Summary: Reminds you to take regular breaks
Name: antirsi
Version: 1.9.2
Release: 1%{?dist}
License: GPL
Group: Applications/
URL: http://tech.inhelsinki.nl/antirsi/

Source: http://tech.inhelsinki.nl/2006-07-08/antirsi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: gtk2-devel
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
AntiRSI is a program (originally for Mac OS X) that helps prevent RSI
(repetitive strain injury) and other computer related stress. It does so by
forcing you to take regular breaks, yet without getting in the way. It also
detects natural breaks so it won't force too many breaks on you.

Note: this version is a preview release of AntiRSI for Gnome.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 gnome/antirsi-gnome %{buildroot}%{_bindir}/antirsi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%{_bindir}/*

%changelog
* Thu Sep 30 2010 Steve Huff <shuff@vecna.org> - 1.9.2-1
- Initial package.
