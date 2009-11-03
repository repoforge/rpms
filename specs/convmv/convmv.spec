# $Id$
# Authority: dries
# Upstream: Björn JACKE <bj$sarnet,de>

Summary: Convert filenames to a different encoding
Name: convmv
Version: 1.14
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://j3e.de/linux/convmv/

Source: http://j3e.de/linux/convmv/convmv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl
Requires: perl

%description
convmv converts filenames (not file content), directories, and even whole 
filesystems to a different encoding. This comes in very handy if, for example, 
one switches from an 8-bit locale to an UTF-8 locale or changes charsets on 
Samba servers. It has some smart features: it automagically recognises if a 
file is already UTF-8 encoded (thus partly converted filesystems can be fully 
moved to UTF-8) and it also takes care of symlinks. Additionally, it is able 
to convert from normalization form C (UTF-8 NFC) to NFD and vice-versa. This 
is important for interoperability with Mac OS X, for example, which uses NFD, 
while Linux and most other Unixes use NFC. Though it's primary written to 
convert from/to UTF-8 it can also be used with almost any other charset 
encoding. Convmv can also be used for case conversion from upper to lower case 
and vice versa with virtually any charset. Note that this is a command line 
tool which requires at least Perl version 5.8.0.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes CREDITS TODO
%doc %{_mandir}/man1/convmv.1*
%{_bindir}/convmv

%changelog
* Fri Dec 12 2008 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Mon Dec 01 2008 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Thu Jan 24 2008 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Thu Jan 24 2008 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 1.10-2
- Fixed group.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
