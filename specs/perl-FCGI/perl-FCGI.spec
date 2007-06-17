# $Id$

# Authority: dries
# Upstream: Sven Verdoolaege <skimo$kotnet,org>


%define real_name FCGI
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Fast CGI module
Name: perl-FCGI
Version: 0.67
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FCGI/

Source: http://www.cpan.org/modules/by-module/FCGI/FCGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is a Fast CGI module for perl. It's based on the FCGI module
that comes with Open Market's FastCGI Developer's Kit, but does
not require you to recompile perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/FCGI/.packlist
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.TERMS README
%{_mandir}/man3/*
%{perl_vendorarch}/FCGI.pm
%{perl_vendorarch}/auto/FCGI/FCGI.bs
%{perl_vendorarch}/auto/FCGI/FCGI.so

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.67-1.2
- Rebuild for Fedora Core 5.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Initial package.
