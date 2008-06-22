# $Id$
# Authority: dag
# Upstream: Graciliano Monteiro Passos <gmpassos$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-MultiType

Summary: Perl Objects as Hash, Array, Scalar, Code and Glob at the same time
Name: perl-Object-MultiType
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-MultiType/

Source: http://www.cpan.org/modules/by-module/Object/Object-MultiType-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Object::MultiType)

%description
Perl Objects as Hash, Array, Scalar, Code and Glob at the same time.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Object::MultiType.3pm*
%dir %{perl_vendorlib}/Object/
#%{perl_vendorlib}/Object/MultiType/
%{perl_vendorlib}/Object/MultiType.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
