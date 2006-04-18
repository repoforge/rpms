# $Id$

# Authority: dag
# Upstream: Petter Nordahl-Hagen <pnordahl$eunet,no>

%define real_version 040818

Summary: Offline NT password and registry editor
Name: chntpw
Version: 0.0.20040818
Release: 1.2
License: GPL
Group: Applications/System
URL: http://home.eunet.no/~pnordahl/ntpasswd/

Source: http://home.eunet.no/~pnordahl/ntpasswd/chntpw-source-%{real_version}.zip
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
%{__make} %{?_smp_mflags} \
	OSSLLIB="%{_libdir}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 chntpw %{buildroot}%{_bindir}/chntpw

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.20040818-1.2
- Rebuild for Fedora Core 5.

* Thu Aug 19 2004 Bert de Bruijn <bert@debruijn.be> - 0.0.20040818-1
- update.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.0.20040116-2
- Cosmetic rebuild for Group-tag.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 0.0.20040116-1
- Initial package. (using DAR)
