# $Id$
# Authority: dries
# Upstream: James E Keenan <jkeenan$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name List-Compare

Summary: Compare elements of two or more lists
Name: perl-List-Compare
Version: 0.33
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-Compare/

Source: http://search.cpan.org/CPAN/authors/id/J/JK/JKEENAN/List-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Compare elements of two or more lists.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/List/Compare.pm
%{perl_vendorlib}/List/Compare

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.32-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
