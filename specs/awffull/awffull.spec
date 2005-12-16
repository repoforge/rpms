# $Id$
# Authority: dries
# Upstream: Steve McInerney <spm$stedee,id,au>

Summary: Web server log analysis program
Name: awffull
Version: 3.01
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.stedee.id.au/awffull

Source: http://www.stedee.id.au/files/awffull-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, libpng-devel, db4-devel, gd-devel

%description
AWFFull is a Web server log analysis program, forked from Webalizer. It 
adds a number of new features and improvements, such as extended frontpage 
history, resizable graphs, and a few more pie charts.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/awffull*
%{_bindir}/awffull

%changelog
* Tue Dec 13 2005 Dries Verachtert <dries@ulyssis.org> - 3.01-1
- Initial package.
