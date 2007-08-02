# $Id$
# Authority: dries
# Upstream: Abigail <$cpan$$abigail,be>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geography-States

Summary: Map states and provinces to their codes and vica versa
Name: perl-Geography-States
Version: 2.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geography-States/

Source: http://search.cpan.org//CPAN/authors/id/A/AB/ABIGAIL/Geography-States-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Map states and provinces to their codes, and vica versa.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/Geography::States*
%{perl_vendorlib}/Geography/States.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
