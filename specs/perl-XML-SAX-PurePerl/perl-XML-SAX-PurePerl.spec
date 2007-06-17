# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX-PurePerl

Summary: XML-SAX-PurePerl Perl module
Name: perl-XML-SAX-PurePerl
Version: 0.80
Release: 0.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX-PurePerl/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-PurePerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

%description
XML-SAX-PurePerl Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/SAX/PurePerl.pm
%{perl_vendorlib}/XML/SAX/PurePerl

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.80-0.2
- Rebuild for Fedora Core 5.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.80-0
- Initial package. (using DAR)
