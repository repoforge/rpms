# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Find-Rule-Perl

Summary: Common rules for searching for Perl things
Name: perl-File-Find-Rule-Perl
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Find-Rule-Perl/

Source: http://www.cpan.org/modules/by-module/File/File-Find-Rule-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
#BuildRequires: perl(ExtUtils::MakeMaker) => 6.42  <- kills el4 build
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) => 0.47
# From yaml requires
BuildRequires: perl(File::Find::Rule) >= 0.20
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(Params::Util) >= 0.38
BuildRequires: perl(Parse::CPAN::Meta) >= 1.38
BuildRequires: perl >= 5.00503


%description
Common rules for searching for Perl things.

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
%doc %{_mandir}/man3/File::Find::Rule::Perl.3pm*
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Find/
%dir %{perl_vendorlib}/File/Find/Rule/
#%{perl_vendorlib}/File/Find/Rule/Perl/
%{perl_vendorlib}/File/Find/Rule/Perl.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 1.09-1
- Updated to version 1.09.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 1.08-1
- Updated to version 1.08.

* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 1.07-1
- Updated to version 1.07.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
