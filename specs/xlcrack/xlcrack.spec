# $Id$
# Authority: dag
# Upstream: 

Summary: Recover lost and forgotten passwords from XLS files
Name: xlcrack
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://devel.tlrmx.org/misc/

Source: http://devel.tlrmx.org/misc/xlcrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgsf-devel

%description
xlcrack is a tool to recover lost and forgotten passwords from XLS files.

xlcrack has been updated to work better with non-ASCII characters, the
passwords displayed in this case should work with Excel installed on
English language and most Western European language systems. On other
systems you may need to type non-ASCII characters differently.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 xlcrack %{buildroot}%{_bindir}/xlcrack

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/xlcrack

%changelog
* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
