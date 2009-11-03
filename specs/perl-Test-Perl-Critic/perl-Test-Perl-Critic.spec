# $Id$
# Authority: dag
# Upstream: Jeffrey Thalhammer <thaljef$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Perl-Critic

Summary: Use Perl::Critic in test scripts
Name: perl-Test-Perl-Critic
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Perl-Critic/

Source: http://www.cpan.org/modules/by-module/Test/Test-Perl-Critic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Use Perl::Critic in test scripts.

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
%doc Changes INSTALL LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Perl::Critic.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/Perl/
#%{perl_vendorlib}/Test/Perl/Critic/
%{perl_vendorlib}/Test/Perl/Critic.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
