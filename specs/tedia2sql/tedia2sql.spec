# $Id$
# Authority: shuff
# Upstream: Tim Ellis <ttiimmeelleessss$tigris,org>

Summary: Visualize database structure with Dia
Name: tedia2sql
Version: 1.2.12
Release: 1%{?dist}
License: GPL
Group: Applications/Database
URL: http://tedia2sql.tigris.org/

Source: http://tedia2sql.tigris.org/files/documents/282/19423/tedia2sql-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: dia >= 0.90
Requires: expat >= 1.95.3
Requires: perl >= 5.006
Requires: perl(Digest::MD5)
Requires: perl(XML::DOM)
Requires: perl(XML::Parser)
Requires: perl(XML::RegExp)

Provides: %{_bindir}/tedia2sql
Provides: config(tedia2sql)

%description
tedia2sql is a tool that allows you to create a database ERD in Dia  (using the
UML shape toolset), then to convert that ERD into a SQL DDL script for multiple
databases. Traditionally, to be able to do these things, you've needed to have
a Win32 OS installed. But because Dia is available for Unices, and because my
Perl script works on Unices, this means that you can now create ERDs that
generate SQL DDL for your database -- all without ever rebooting into Win32!

%prep
%setup -n %{name}

%build
# no build necessary

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_sysconfdir}
%{__install} -m0755 tedia2sql %{buildroot}%{_bindir}
%{__install} -m0644 tedia2sqlrc %{buildroot}%{_sysconfdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README www/
%{_bindir}/*
%{_sysconfdir}/*

%changelog
* Thu Mar 11 2010 Steve Huff <shuff@vecna.org> - 1.2.12-1
- Initial package.
