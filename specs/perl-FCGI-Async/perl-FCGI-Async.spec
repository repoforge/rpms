# $Id$
# Authority: dries
# Upstream: Paul Evans <leonerd$leonerd,org,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name FCGI-Async

Summary: Allows FastCGI asynchronously
Name: perl-FCGI-Async
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FCGI-Async/

Source: http://search.cpan.org//CPAN/authors/id/P/PE/PEVANS/FCGI-Async-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Module to allow use of FastCGI asynchronously.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/FCGI::Async*
%{perl_vendorlib}/FCGI/Async.pm
%{perl_vendorlib}/FCGI/Async/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
