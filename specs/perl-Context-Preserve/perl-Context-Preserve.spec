# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Context-Preserve

Summary: Run code after a subroutine call, preserving the context
Name: perl-Context-Preserve
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Context-Preserve/

#Source: http://www.cpan.org/modules/by-module/Context/Context-Preserve-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/J/JR/JROCKWAY/Context-Preserve-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(ok)

%description
Run code after a subroutine call, preserving the context the subroutine would
have seen if it were the last statement in the caller.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml
%doc %{_mandir}/man3/Context::Preserve.3pm*
%dir %{perl_vendorlib}/Context/
#%{perl_vendorlib}/Context/Preserve/
%{perl_vendorlib}/Context/Preserve.pm

%changelog
* Mon Mar 22 2010 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
