# $Id$
# Authority: matthias

%define real_name XML-DOM
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl module for building DOM Level 1 compliant document structures
Name: perl-XML-DOM
Version: 1.43
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-DOM/
Source: http://www.cpan.org/modules/by-module/XML/XML-DOM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl
BuildArch: noarch

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to XML::Parser,
called 'Dom', that allows XML::Parser to build an Object Oriented datastructure
with a DOM Level 1 compliant interface.
For a description of the DOM (Document Object Model), see :
http://www.w3.org/DOM/


%prep
%setup -n %{real_name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*{,/*}/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/DOM/
%{perl_vendorlib}/XML/DOM.pm
%{perl_vendorlib}/XML/Handler/BuildDOM.pm


%changelog
* Fri Dec 17 2004 Matthias Saou <http://freshrpms.net/> 1.43-1
- Initial package based on Dries' perl-XML-RegExp spec file.

