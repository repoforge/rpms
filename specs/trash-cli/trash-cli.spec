# $Id: $
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Command line interface to the FreeDesktop.org trashcan
Name: trash-cli
Version: 0.11.2
Release: 1
License: GPLv2
Group: Applications/File
URL: http://code.google.com/p/trash-cli/

Source: http://trash-cli.googlecode.com/files/trash-cli-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel
Requires: python-unipath

%description
trash-cli is a command line interface to the FreeDesktop.org trashcan. It 
implements the FreeDesktop.org trash specification. For each trashed file, 
it will remember the name, original path, date of deletion, and permissions. 
It interoperates with KDE Trash, and is CLI compatible with the rm command.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__mkdir} -p %{buildroot}%{_mandir}/man1/
%{__mv} %{buildroot}%{_prefix}/man/man1/trash-* %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING THANKS *.txt
%doc %{_mandir}/man1/trash-empty.1*
%doc %{_mandir}/man1/trash-list.1*
%doc %{_mandir}/man1/trash-put.1*
%doc %{_mandir}/man1/trash-restore.1*
%{_bindir}/restore-trash
%{_bindir}/trash-empty
%{_bindir}/trash-list
%{_bindir}/trash-put
%{_bindir}/trash-restore
%{_bindir}/volume-of
%{python_sitearch}/trashcli/
%{python_sitearch}/trash_cli-%{version}-*.egg-info/

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 0.11.2-1
- Updated to release 0.11.2.

* Fri Jul 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.1.10.0.41-1
- Initial package.
