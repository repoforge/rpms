# $Id$
# Authority: dries
# Upstream: Joshua ben Jore <jjore$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Deadly

Summary: Object that dies whenever examined
Name: perl-Object-Deadly
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Deadly/

Source: http://search.cpan.org//CPAN/authors/id/J/JJ/JJORE/Object-Deadly-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Object that dies whenever examined

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
%doc Changes README
%doc %{_mandir}/man3/Object::Deadly*
%{perl_vendorlib}/Object/Deadly.pm
%{perl_vendorlib}/Object/Deadly/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
