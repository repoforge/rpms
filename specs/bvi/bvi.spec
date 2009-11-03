# $Id$
# Authority: dag

Summary: Hex editor for binary files (binary vi)
Name: bvi
Version: 1.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://bvi.sourceforge.net/

Source: http://dl.sf.net/bvi/bvi-%{version}.src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
bvi is a display-oriented editor for binary files, based on the vi texteditor.

%prep
%setup  

%build 
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS README html/
%doc %{_mandir}/man1/bmore.1*
%doc %{_mandir}/man1/bvi.1*
%{_bindir}/bmore
%{_bindir}/bvedit
%{_bindir}/bvi
%{_bindir}/bview
%{_libdir}/bmore.help

%changelog
* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Initial package. (using DAR)
