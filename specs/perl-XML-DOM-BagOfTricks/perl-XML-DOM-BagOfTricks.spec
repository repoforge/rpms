# $Id$
# Authority: dries
# Upstream: Aaron James Trevena <TeeJay-cpan$droogs,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-DOM-BagOfTricks

Summary: Functions for dealing with DOM trees
Name: perl-XML-DOM-BagOfTricks
Version: 0.05
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-DOM-BagOfTricks/

Source: http://search.cpan.org/CPAN/authors/id/T/TE/TEEJAY/XML-DOM-BagOfTricks-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
XML::DOM::BagOfTricks provides a bundle, or bag, of functions that make
dealing with and creating DOM objects easier.

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
%{perl_vendorlib}/XML/DOM/BagOfTricks.pm
%{perl_vendorlib}/auto/XML/DOM/BagOfTricks/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
