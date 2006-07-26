# $Id$
# Authority: dries
# Upstream: Pavel Hlavnicka <cpanuser$seznam,cz>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Sablotron

Summary: Encapsulation of the Sablotron XSLT processor
Name: perl-XML-Sablotron
Version: 1.01
Release: 1
License: MPL/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Sablotron/

Source: http://search.cpan.org/CPAN/authors/id/P/PA/PAVELH/XML-Sablotron-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, sablotron-devel
BuildRequires: expat-devel >= 1.95.2

%description
XML::Sablotron is a simple Perl package, which encapsulates the C API
of Sablotron XSLT processor.

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
%doc %{_mandir}/man3/*
%{perl_vendorarch}/XML/Sablotron.pm
%{perl_vendorarch}/XML/Sablotron/
%{perl_vendorarch}/auto/XML/Sablotron/

%changelog
* Wed Jul 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
