# $Id$
# Authority: dries
# Upstream: Ricky Buchanan <rb$tertius,net,au>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-LineEditor

Summary: Simple line editor
Name: perl-Text-LineEditor
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-LineEditor/

Source: http://search.cpan.org/CPAN/authors/id/G/GO/GOSSAMER/Text-LineEditor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements a -very- simple editor like Berkley mail used
to use.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
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
%{perl_vendorlib}/Text/LineEditor.pm
%{perl_vendorlib}/Text/example.pl

%changelog
* Sun Apr  3 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
