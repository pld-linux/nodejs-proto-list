%define		pkg	proto-list
Summary:	A list of objects bound by prototype chain
Name:		nodejs-%{pkg}
Version:	1.2.2
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/proto-list
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	ecd652b4aa9724ee1ca902599dd8deac
#BuildRequires:  nodejs-tap
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A list of objects bound by prototype chain. Used for the Node.js
package manager (npm) configuration.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

# We currently don't run tests because I'd have to file another ten or
# so review reuqests for the node.js TAP testing framework and methinks there
# are enough of those for now.  ;-)
##%%check
##%%nodejs %{pkg}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{nodejs_libdir}/%{pkg}
