# $Id$

# Authority: dries
# Upstream: Jean-Michel Hiver <jhiver$mkdoc,com>

%define real_name MKDoc-XML
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: MKDoc XML Toolkit
Name: perl-MKDoc-XML
Version: 0.75
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MKDoc-XML/

Source: http://www.cpan.org/modules/by-module/MKDoc/MKDoc-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Typically, in MKDoc the stripper is used to remove unwanted presentational
markup while the tagger adds structural markup such as an abbr tag or automatically
hyperlinks expressions so that MKDoc users don't have to know about a tag syntax.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/MKDoc/XML.pm
%{perl_vendorlib}/MKDoc/XML/*

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.75-1
- Updated to release 0.75.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.74-1
- Updated to release 0.74.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.72-1
- Initial package.
