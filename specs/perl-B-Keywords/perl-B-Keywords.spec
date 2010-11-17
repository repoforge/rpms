# $Id$
# Authority: dag
# Upstream: Joshua ben Jore <jjore$cpan,org>

### EL6 ships with perl-B-Keywords-1.09-3.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Keywords

Summary: Perl module with lists of reserved barewords and symbol names
Name: perl-B-Keywords
Version: 1.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Keywords/

Source: http://search.cpan.org/CPAN/authors/id/J/JJ/JJORE/B-Keywords-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
B-Keywords is a perl module with lists of reserved barewords and symbol names.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/B::Keywords.3pm*
%dir %{perl_vendorlib}/B/
%{perl_vendorlib}/B/Keywords.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.09-1
- Updated to version 1.09.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
