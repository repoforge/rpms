# $Id$

# Authority: dag
# Upstream: Petter Nordahl-Hagen <pnordahl@eunet.no>

%define rversion 040116

Summary: Offline NT password and registry editor.
Name: chntpw
Version: 0.0.20040116
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://home.eunet.no/~pnordahl/ntpasswd/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://home.eunet.no/~pnordahl/ntpasswd/chntpw-source-%{rversion}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: openssl-devel

%description
chntpw is a utility to (re)set the password of any user that has a valid
(local) account on your NT system, by modifying the crypted password in
the registrys SAM file.

You do not need to know the old password to set a new one. It detects and
offers to unlock locked or disabled out user accounts!

It works offline, that is, you have to shutdown your computer and boot off
a floppydisk or CD. The bootdisk includes stuff to access NTFS partitions
and scripts to glue the whole thing together.

%prep
%setup -c

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 chntpw %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/*

%changelog
* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 0.0.20040116-1
- Initial package. (using DAR)
