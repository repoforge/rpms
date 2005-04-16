# $Id$
# Authority: dries
# Upstream: Uri Guttman <uri$sysarch,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-ReadBackwards

Summary: Read a file backwards by lines
Name: perl-File-ReadBackwards
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-ReadBackwards/

Source: http://search.cpan.org/CPAN/authors/id/U/UR/URI/File-ReadBackwards-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module reads a file backwards line by line. It is simple to use,
memory efficient and fast. It supports both an object and a tied handle
interface.

It is intended for processing log and other similar text files which
typically have their newest entries appended to them. By default files
are assumed to be plain text and have a line ending appropriate to the
OS. But you can set the input record separator string on a per file
basis.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/File/ReadBackwards.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
