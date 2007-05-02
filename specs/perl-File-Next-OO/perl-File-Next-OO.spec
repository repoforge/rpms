# $Id$
# Authority: dries
# Upstream: Boris Zentner <bzm$2bz,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Next-OO

Summary: File-finding iterator Wrapper for File::Next::files
Name: perl-File-Next-OO
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Next-OO/

Source: http://search.cpan.org//CPAN/authors/id/B/BO/BORISZ/File-Next-OO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
File-finding iterator Wrapper for File::Next::files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/File/Next/
%{perl_vendorlib}/File/Next/OO.pm

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
