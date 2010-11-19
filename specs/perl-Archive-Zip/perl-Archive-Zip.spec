# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk@cpan.org>

### EL6 ships with perl-Archive-Zip-1.30-2.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-Archive-Zip-1.16-1.2.1
%{?el5:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Zip

Summary: Provide an interface to ZIP archive files
Name: perl-Archive-Zip
Version: 1.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Zip/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Archive-Zip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Compress::Raw::Zlib) >= 2.017
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IO::Seekable)
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Time::Local)
BuildRequires: perl >= 5.00396
Requires: perl(Compress::Raw::Zlib) >= 2.017
Requires: perl(File::Basename)
Requires: perl(File::Copy)
Requires: perl(File::Find)
Requires: perl(File::Path)
Requires: perl(File::Spec) >= 0.80
Requires: perl(File::Temp)
Requires: perl(IO::File)
Requires: perl(IO::Handle)
Requires: perl(IO::Seekable)
Requires: perl(Test::More) >= 0.42
Requires: perl(Time::Local)
Requires: perl >= 5.00396

%filter_from_requires /^perl*/d
%filter_setup


%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.

Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### FIXME: Change to real perl location. (Please fix upstream)
%{__perl} -pi -e 's|^#!/.*bin/perl|#!%{__perl}|i;' examples/*.pl

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Archive::Zip.3pm*
%doc %{_mandir}/man3/Archive::Zip::*.3pm*
%{_bindir}/crc32
%dir %{perl_vendorlib}/Archive/
%{perl_vendorlib}/Archive/Zip/
%{perl_vendorlib}/Archive/Zip.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.30-1
- Updated to version 1.30.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 1.26-1
- Updated to release 1.26.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.20-1
- Disabled auto-requires for examples/.

* Wed Jul 13 2005 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.09-0
- Updated to release 1.09.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.05-0
- Initial package. (using DAR)
