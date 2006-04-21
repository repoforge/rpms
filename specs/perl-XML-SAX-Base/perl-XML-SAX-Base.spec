# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX-Base

Summary: XML-SAX-Base Perl module
Name: perl-XML-SAX-Base
Version: 1.04
Release: 0.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX-Base/

Source: http://search.cpan.org/CPAN/authors/id/K/KH/KHAMPTON/XML-SAX-Base-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
XML-SAX-Base Perl module.

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
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/SAX/Base.pm
%{perl_vendorlib}/XML/SAX/Exception.pm
%{perl_vendorlib}/XML/SAX/placeholder.pl

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-0.2
- Rebuild for Fedora Core 5.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.04-0
- Initial package. (using DAR)
