# $Id$
# Authority: dries
# Upstream: Tassilo von Parseval <tassilo,parseval$post,rwth-aachen,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-MboxParser

Summary: Read-only access to UNIX-mailboxes
Name: perl-Mail-MboxParser
Version: 0.54
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-MboxParser/

Source: http://search.cpan.org/CPAN/authors/id/V/VP/VPARSEVAL/Mail-MboxParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Mail::MboxParser is a module for working with UNIX-flavoured mailboxes.

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
%doc Changelog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Mail/MboxParser.pm
%{perl_vendorlib}/Mail/MboxParser

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
