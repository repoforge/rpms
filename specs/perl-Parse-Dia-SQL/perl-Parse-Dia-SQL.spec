# $Id$
# Authority: shuff
# Upstream: Andreas Faafeng <aff$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Dia-SQL

Summary: Convert Dia class diagrams into SQL
Name: perl-%{real_name}
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-Dia-SQL/

Source: http://search.cpan.org/CPAN/authors/id/A/AF/AFF/Parse-Dia-SQL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Fatal)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::Uncompress::Gunzip)
BuildRequires: perl(Log::Dispatch::FileRotate)
BuildRequires: perl(Log::Log4perl)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Table)
BuildRequires: perl(XML::DOM)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::Dumper)
Requires: perl(Digest::MD5)
Requires: perl(Fatal)
Requires: perl(File::Find)
Requires: perl(File::Spec::Functions)
Requires: perl(File::Temp)
Requires: perl(Getopt::Long)
Requires: perl(IO::Uncompress::Gunzip)
Requires: perl(Log::Dispatch::FileRotate)
Requires: perl(Log::Log4perl)
Requires: perl(POSIX)
Requires: perl(Text::Table)
Requires: perl(XML::DOM)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Dia is a diagram creation program for Linux, Unix and Windows released under
the GNU General Public License.  Parse::Dia::SQL converts Dia class diagrams
into SQL.  Parse::Dia::SQL is the parser that interprets the .dia file(s) into
an internal datastructure.  Parse::Dia::SQL::Output (or one of its sub classes)
can take the datastructure and generate the SQL statements it represents.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes MANIFEST README TODO
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Parse/Dia/
%{perl_vendorlib}/Parse/Dia/*
%{_bindir}/*

%changelog
* Tue Mar 23 2010 Steve Huff <shuff@vecna.org> - 0.14-1
- Initial package.
