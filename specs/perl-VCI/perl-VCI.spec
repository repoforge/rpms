# $Id$
# Authority: shuff
# Upstream: Max Kanat-Alexander <mkanat$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name VCI

Summary: A library for interacting with various version-control systems
Name: perl-VCI
Version: 0.6.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/VCI/

Source: http://search.cpan.org/CPAN/authors/id/M/MK/MKANAT/VCI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.6.0
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::DateParse)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IPC::Cmd) >= 0.42
BuildRequires: perl(IPC::Run) >= 0.55
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Load::Conditional) >= 0.24
BuildRequires: perl(Module::Install)
BuildRequires: perl(Moose) >= 0.27
BuildRequires: perl(MooseX::Method)
BuildRequires: perl(Path::Abstract) >= 0.093
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Text::Diff::Parser) >= 0.07
BuildRequires: perl(XML::Simple)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.6.0
Requires: perl(Carp)
Requires: perl(Cwd)
Requires: perl(DateTime)
Requires: perl(DateTime::Format::DateParse)
Requires: perl(File::Path)
Requires: perl(File::Temp)
Requires: perl(Git)
Requires: perl(IPC::Cmd) >= 0.42
Requires: perl(IPC::Run) >= 0.55
Requires: perl(LWP::UserAgent)
Requires: perl(List::Util)
Requires: perl(Module::Load::Conditional) >= 0.24
Requires: perl(Module::Install)
Requires: perl(Moose) >= 0.27
Requires: perl(MooseX::Method)
Requires: perl(Path::Abstract) >= 0.093
Requires: perl(SVN::Core) >= 1.2.0
Requires: perl(Text::Diff::Parser) >= 0.07
Requires: perl(XML::Simple)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is VCI, the generic Version Control Interface. The goal of VCI is to
create a common API that can interface with all version control systems (which
are sometimes also called Software Configuration Management or "SCM" systems).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/VCI.pm
%{perl_vendorlib}/VCI/*
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Wed Aug 25 2010 Steve Huff <shuff@vecna.org> - 0.6.1-1
- Initial package.
