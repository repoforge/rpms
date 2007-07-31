# $Id$
# Authority: dag
# Upstream: Marcus Ramberg <mramberg$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Runtime

Summary: Catalyst  Runtime version
Name: perl-Catalyst-Runtime
Version: 5.7007
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Runtime/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Runtime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1, perl(ExtUtils::MakeMaker)
# this module seems to require 50% of cpan..
BuildRequires: perl(Class::Accessor::Fast), perl(Class::Inspector)
BuildRequires: perl(CGI::Simple::Cookie), perl(Data::Dump)
BuildRequires: perl(File::Modified), perl(HTML::Entities), perl(HTTP::Body)
BuildRequires: perl(HTTP::Headers), perl(HTTP::Request), perl(HTTP::Response)
BuildRequires: perl(HTTP::Request::AsCGI), perl(LWP::UserAgent)
BuildRequires: perl(Module::Pluggable), perl(Path::Class), perl(Scalar::Util)
BuildRequires: perl(Text::SimpleTable), perl(Tree::Simple)
BuildRequires: perl(Tree::Simple::Visitor::FindByPath), perl(URI)
BuildRequires: perl(Class::Data::Inheritable)

%description
Catalyst  Runtime version.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man1/catalyst.pl.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/catalyst.pl
%{perl_vendorlib}/Catalyst/
%{perl_vendorlib}/Catalyst.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 5.7007-1
- Initial package. (using DAR)
